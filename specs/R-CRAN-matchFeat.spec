%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matchFeat
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          One-to-One Feature Matching

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-utils 

%description
Statistical methods to match feature vectors between multiple datasets in
a one-to-one fashion. Given a fixed number of classes/distributions, for
each unit, exactly one vector of each class is observed without label. The
goal is to label the feature vectors using each label exactly once so to
produce the best match across datasets, e.g. by minimizing the variability
within classes. Statistical solutions based on empirical loss functions
and probabilistic modeling are provided. The 'Gurobi' software and its 'R'
interface package are required for one of the package functions
(match.2x()) and can be obtained at <https://www.gurobi.com/> (free
academic license). For more details, refer to Degras (2022)
<doi:10.1080/10618600.2022.2074429> "Scalable feature matching for large
data collections" and Bandelt, Maas, and Spieksma (2004)
<doi:10.1057/palgrave.jors.2601723> "Local search heuristics for
multi-index assignment problems with decomposable costs".

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
