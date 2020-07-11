%global packname  EPX
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Ensemble of Phalanxes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-rngtools 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-randomForest 
Requires:         R-nnet 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-rngtools 

%description
An ensemble method for the statistical detection of a rare class in
two-class classification problems. The method uses an ensemble of
classifiers where the constituent models of the ensemble use disjoint
subsets (phalanxes) of explanatory variables. We provide an implementation
of the phalanx-formation algorithm. Please see Tomal et al. (2015)
<doi:10.1214/14-AOAS778>, Tomal et al. (2016)
<doi:10.1021/acs.jcim.5b00663>, and Tomal et al. (2019) <arXiv:1706.06971>
for more details.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
