%global packname  REPLesentR
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Presentations in the REPL

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.21
BuildRequires:    R-CRAN-modules 
BuildRequires:    R-CRAN-dat 
BuildRequires:    R-tools 
Requires:         R-CRAN-knitr >= 1.21
Requires:         R-CRAN-modules 
Requires:         R-CRAN-dat 
Requires:         R-tools 

%description
Create presentations and display them inside the R 'REPL' (Read-Eval-Print
loop), aka the R console. Presentations can be written in 'RMarkdown' or
any other text format. A set of convenient navigation options as well as
code evaluation during a presentation is provided. It is great for tech
talks with live coding examples and tutorials. While this is not a
replacement for standard presentation formats, it's old-school looks might
just be what sets it apart. This project has been inspired by the
'REPLesent' project for presentations in the 'Scala' 'REPL'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
