%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  controlfunctionIV
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Control Function Methods with Possibly Invalid Instrumental Variables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dr 
BuildRequires:    R-CRAN-orthoDr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-dr 
Requires:         R-CRAN-orthoDr 
Requires:         R-stats 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-Formula 

%description
Inference with control function methods for nonlinear outcome models when
the model is known ('Guo and Small' (2016) <arXiv:1602.01051>) and when
unknown but semiparametric ('Li and Guo' (2021) <arXiv:2010.09922>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
