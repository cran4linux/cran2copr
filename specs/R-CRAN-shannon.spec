%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shannon
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Entropy Measures and Relative Loss

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VaRES 
BuildRequires:    R-CRAN-extraDistr 
Requires:         R-stats 
Requires:         R-CRAN-VaRES 
Requires:         R-CRAN-extraDistr 

%description
The functions allow for the numerical evaluation of some commonly used
entropy measures, such as Shannon entropy, Rényi entropy, Havrda and
Charvat entropy, and Arimoto entropy, at selected parametric values from
several well-known and widely used probability distributions. Moreover,
the functions also compute the relative loss of these entropies using the
truncated distributions. Related works include: Awad, A. M., & Alawneh, A.
J. (1987). Application of entropy to a life-time model. IMA Journal of
Mathematical Control and Information, 4(2), 143-148.
<doi:10.1093/imamci/4.2.143>.

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
