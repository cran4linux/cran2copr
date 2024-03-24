%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stylest2
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Speakers of Texts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-quanteda 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-quanteda 

%description
Estimates the authors or speakers of texts. Methods developed in Huang,
Perry, and Spirling (2020) <doi:10.1017/pan.2019.49>. The model is built
on a Bayesian framework in which the distinctiveness of each speaker is
defined by how different, on average, the speaker's terms are to everyone
else in the corpus of texts. An optional cross-validation method is
implemented to select the subset of terms that generate the most accurate
speaker predictions. Once a set of terms is selected, the model can be
estimated. Speaker distinctiveness and term influence can be recovered
from parameters in the model using package functions. Once fitted, the
model can be used to predict authorship of new texts.

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
