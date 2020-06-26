%global packname  DynareR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          A Seamless Integration of 'R' and 'Dynare'

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.20
Requires:         R-CRAN-knitr >= 1.20

%description
It allows running 'Dynare' program from R Markdown. 'Dynare' is a software
platform for handling a wide class of economic models, in particular
dynamic stochastic general equilibrium ('DSGE') and overlapping
generations ('OLG') models.  This package serves as a 'Dynare' Knit-Engine
for 'knitr' package. The package requires 'Dynare' 4.6.1
(<https://dynare.org>) and 'Octave' 5.2.0
(<https://www.gnu.org/software/octave/download.html>).  Write all your
'Dynare' commands in R Markdown chunk.

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
