%global packname  ADMUR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Ancient Demographic Modelling Using Radiocarbon

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-zoo 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mathjaxr 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-zoo 

%description
Provides tools to directly model underlying population dynamics using date
datasets (radiocarbon and other) with a Continuous Piecewise Linear (CPL)
model framework. Various other model types included. Taphonomic loss
included optionally as a power function. Model comparison framework using
BIC. Package also calibrates 14C samples, generates Summed Probability
Distributions (SPD), and performs SPD simulation analysis to generate a
Goodness-of-fit test for the best selected model. Details about the method
can be found in Timpson A., Barberena R., Thomas M. G., Mendez C., Manning
K. (2020) <doi:10.1098/rstb.2019.0723>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
