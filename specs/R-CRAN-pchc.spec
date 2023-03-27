%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pchc
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Network Learning with the PCHC and Related Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bigstatsr 
BuildRequires:    R-CRAN-bnlearn 
BuildRequires:    R-CRAN-dcov 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
Requires:         R-CRAN-bigstatsr 
Requires:         R-CRAN-bnlearn 
Requires:         R-CRAN-dcov 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 

%description
Bayesian network learning using the PCHC algorithm. PCHC stands for PC
Hill-Climbing, a new hybrid algorithm that uses PC to construct the
skeleton of the BN and then applies the Hill-Climbing greedy search. More
algorithms and variants have been added, such as MMHC, FEDHC, and the Tabu
search variants, PCTABU, MMTABU and FEDTABU. The relevant papers are a)
Tsagris M. (2021). A new scalable Bayesian network learning algorithm with
applications to economics. Computational Economics, 57(1): 341-367.
<doi:10.1007/s10614-020-10065-7>. b) Tsagris M. (2022). The FEDHC Bayesian
Network Learning Algorithm. Mathematics 2022, 10(15): 2604.
<doi:10.3390/math10152604>.

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
