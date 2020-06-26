%global packname  RcppCWB
%global packver   0.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}
Summary:          'Rcpp' Bindings for the 'Corpus Workbench' ('CWB')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    bison
BuildRequires:    flex
BuildRequires:    pcre >= 7
BuildRequires:    glib2-devel
BuildRequires:    ncurses-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-Rcpp >= 0.12.6

%description
'Rcpp' Bindings for the C code of the 'Corpus Workbench' ('CWB'), an
indexing and query engine to efficiently analyze large corpora
(<http://cwb.sourceforge.net>). 'RcppCWB' is licensed under the GNU GPL-3,
in line with the GPL-3 license of the 'CWB'
(<https://www.r-project.org/Licenses/GPL-3>). The 'CWB' relies on 'pcre'
(BSD license, see <https://www.pcre.org/licence.txt>) and 'GLib' (LGPL
license, see <https://www.gnu.org/licenses/lgpl-3.0.en.html>). See the
file LICENSE.note for further information. The package includes modified
code of the 'rcqp' package (GPL-2, see
<https://cran.r-project.org/package=rcqp>). The original work of the
authors of the 'rcqp' package is acknowledged with great respect, and they
are listed as authors of this package. To achieve cross-platform
portability (including Windows), using 'Rcpp' for wrapper code is the
approach used by 'RcppCWB'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && find %{packname} -name Makefile -exec sed -i '/^all:.*/i CFLAGS+=-fcommon' {} \;
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
