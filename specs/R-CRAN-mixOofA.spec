%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixOofA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis of Order-of-Addition Mixture Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doofa 
BuildRequires:    R-CRAN-crossdes 
BuildRequires:    R-CRAN-mixexp 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-Rsolnp 
Requires:         R-CRAN-doofa 
Requires:         R-CRAN-crossdes 
Requires:         R-CRAN-mixexp 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-Rsolnp 

%description
A facility to generate various classes of fractional designs for
order-of-addition experiments namely fractional order-of-additions
orthogonal arrays, see Voelkel, Joseph G. (2019). "The design of
order-of-addition experiments." Journal of Quality Technology 51:3,
230-241, <doi:10.1080/00224065.2019.1569958>. Provides facility to
construct component orthogonal arrays, see Jian-Feng Yang, Fasheng Sun and
Hongquan Xu (2020). "A Component Position Model, Analysis and Design for
Order-of-Addition Experiments." Technometrics,
<doi:10.1080/00401706.2020.1764394>. Supports generation of fractional
designs for order-of-addition mixture experiments. Analysis of data from
order-of-addition mixture experiments is also supported.

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
