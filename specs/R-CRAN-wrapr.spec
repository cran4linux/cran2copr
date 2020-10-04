%global packname  wrapr
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Wrap R Tools for Debugging and Parametric Programming

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 

%description
Tools for writing and debugging R code. Provides: '%.>%' dot-pipe (an 'S3'
configurable pipe), unpack/to (R style multiple assignment/return),
'build_frame()'/'draw_frame()' ('data.frame' example tools), 'qc()'
(quoting concatenate), ':=' (named map builder), 'let()' (converts
non-standard evaluation interfaces to parametric standard evaluation
interfaces, inspired by 'gtools::strmacro()' and 'base::bquote()'), and
more.

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
