%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  careless
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Procedures for Computing Indices of Careless Responding

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-psych 

%description
When taking online surveys, participants sometimes respond to items
without regard to their content. These types of responses, referred to as
careless or insufficient effort responding, constitute significant
problems for data quality, leading to distortions in data analysis and
hypothesis testing, such as spurious correlations. The 'R' package
'careless' provides solutions designed to detect such careless /
insufficient effort responses by allowing easy calculation of indices
proposed in the literature. It currently supports the calculation of
longstring, even-odd consistency, psychometric synonyms/antonyms,
Mahalanobis distance, and intra-individual response variability (also
termed inter-item standard deviation). For a review of these methods, see
Curran (2016) <doi:10.1016/j.jesp.2015.07.006>.

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
