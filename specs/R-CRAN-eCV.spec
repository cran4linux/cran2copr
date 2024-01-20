%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eCV
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Enhanced Coefficient of Variation and IDR Extensions for Reproducibility Assessment

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future.apply >= 1.9.0
BuildRequires:    R-CRAN-future >= 1.4.0
BuildRequires:    R-CRAN-idr >= 1.3
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-future.apply >= 1.9.0
Requires:         R-CRAN-future >= 1.4.0
Requires:         R-CRAN-idr >= 1.3
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-stats 
Requires:         R-utils 

%description
Reproducibility assessment is essential in extracting reliable scientific
insights from high-throughput experiments.  While the Irreproducibility
Discovery Rate (IDR) method has been instrumental in assessing
reproducibility, its standard implementation is constrained to handling
only two replicates. Package 'eCV' introduces an enhanced Coefficient of
Variation (eCV) metric to assess the likelihood of omic features being
reproducible. Additionally, it offers alternatives to the Irreproducible
Discovery Rate (IDR) calculations for multi-replicate experiments. These
tools are valuable for analyzing high-throughput data in genomics and
other omics fields. The methods implemented in 'eCV' are described in
Gonzalez-Reymundez et al., (2023) <doi:10.1101/2023.12.18.572208>.

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
