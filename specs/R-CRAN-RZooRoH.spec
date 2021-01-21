%global packname  RZooRoH
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Partitioning of Individual Autozygosity into Multiple Homozygous-by-Descent Classes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-iterators 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-iterators 

%description
Functions to identify Homozygous-by-Descent (HBD) segments associated with
runs of homozygosity (ROH) and to estimate individual autozygosity (or
inbreeding coefficient). HBD segments and autozygosity are assigned to
multiple HBD classes with a model-based approach relying on a mixture of
exponential distributions. The rate of the exponential distribution is
distinct for each HBD class and defines the expected length of the HBD
segments. These HBD classes are therefore related to the age of the
segments (longer segments and smaller rates for recent autozygosity /
recent common ancestor). The functions allow to estimate the parameters of
the model (rates of the exponential distributions, mixing proportions), to
estimate global and local autozygosity probabilities and to identify HBD
segments with the Viterbi decoding. The method is fully described in Druet
and Gautier (2017) <doi:10.1111/mec.14324>.

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
