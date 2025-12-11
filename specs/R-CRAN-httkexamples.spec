%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  httkexamples
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          High-Throughput Toxicokinetics Examples

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-httk 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-httk 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-Rdpack 

%description
High throughput toxicokinetics ("HTTK") is the combination of 1)
chemical-specific in vitro measurements or in silico predictions and 2)
generic mathematical models, to predict absorption, distribution,
metabolism, and excretion by the body. HTTK methods have been described by
Pearce et al. (2017) (<doi:10.18637/jss.v079.i04>) and Breen et al. (2021)
(<doi:10.1080/17425255.2021.1935867>). Here we provide examples
(vignettes) applying HTTK to solve various problems in bioinformatics,
toxicology, and exposure science. In accordance with Davidson-Fritz et al.
(2025) (<doi:10.1371/journal.pone.0321321>), whenever a new HTTK model is
developed, the code to generate the figures evaluating that model is added
as a new vignettte.

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
