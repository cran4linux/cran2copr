%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExNRuleEnsemble
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A k Nearest Neibour Ensemble Based on Extended Neighbourhood Rule

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-FNN 

%description
The extended neighbourhood rule for the k nearest neighbour ensemble where
the neighbours are determined in k steps. Starting from the first nearest
observation of the test point, the algorithm identifies a single
observation that is closest to the observation at the previous step. At
each base learner in the ensemble, this search is extended to k steps on a
random bootstrap sample with a random subset of features selected from the
feature space. The final predicted class of the test point is determined
by using a majority vote in the predicted classes given by all base
models. Amjad Ali, Muhammad Hamraz, Naz Gul, Dost Muhammad Khan, Saeed
Aldahmani, Zardad Khan (2022) <doi:10.48550/arXiv.2205.15111>.

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
