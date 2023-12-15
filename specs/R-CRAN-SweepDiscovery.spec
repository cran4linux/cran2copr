%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SweepDiscovery
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Selective Sweep Discovery Tool

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-randomForest 

%description
Selective sweep is a biological phenomenon in which genetic variation
between neighboring beneficial mutant alleles is swept away due to the
effect of genetic hitchhiking. Detection of selective sweep is not well
acquainted as well as it is a laborious job. This package is a user
friendly approach for detecting selective sweep in genomic regions. It
uses a Random Forest based machine learning approach to predict selective
sweep from VCF files as an input. Input of this function, train data and
new data, can be computed using the project
<https://github.com/AbhikSarkar1999/SweepDiscovery> in 'GitHub'. This
package has been developed by using the concept of Pavlidis and Alachiotis
(2017) <doi:10.1186/s40709-017-0064-0>.

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
