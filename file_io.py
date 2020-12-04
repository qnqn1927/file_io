"""
file_io.py
ファイル入出力管理用モジュール
"""
import os
import sys

# 入出力ファイル設定
# ===
# io_path: ファイル入出力用のフォルダ
# in_basename: 入力ファイル特定用の接頭辞をリスト型で渡す
# out_basename: 出力ファイル名称をリスト型で渡す
def fn_get_filenames(io_path, in_basename, out_basename):
    io_filenames = {
        'in' : fn_make_input_list(io_path, in_basename),
        'out' : fn_make_output_list(io_path, out_basename)
    }
    return io_filenames

# 入力ファイル名生成
# ===
def fn_make_input_list(io_path, basename):
    # ディレクトリ内のアイテム取得
    directory_items = os.listdir(io_path)
    target_filenames = []

    for input_filename in basename:
        target_filename = [x for x in directory_items if x.startswith(input_filename)]
        # 処理対象が存在しないもしくは2つ以上あり特定できない場合はエラーとして処理中止
        if len(target_filename) != 1: print('処理対象のファイルが正しく与えられていません'); exit()
        target_filenames.append(io_path + target_filename[0])

    return target_filenames

# 出力ファイル名生成
# ===
def fn_make_output_list(io_path, basename):
    return [io_path + x + '.csv' for x in basename]

# 拡張子の前に文字列を挿入
# ===
def fn_insert_strings_before_extension(str, io_filename):
    path, ext = os.path.splitext(io_filename)
    return path + str + ext