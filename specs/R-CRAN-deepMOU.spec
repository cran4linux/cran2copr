%global packname  deepMOU
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clustering of Short Texts by Mixture of Unigrams and Its Deep Extensions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-skmeans 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-skmeans 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 

%description
Functions providing an easy and intuitive way for fitting and clusters
data using the Mixture of Unigrams models by means the
Expectation-Maximization algorithm (Nigam, K. et al. (2000).
<doi:10.1023/A:1007692713085>), Mixture of Dirichlet-Multinomials
estimated by Gradient Descent (Anderlucci, Viroli (2020)
<doi:10.1007/s11634-020-00399-3>) and Deep Mixture of Multinomials whose
estimates are obtained with Gibbs sampling scheme (Viroli, Anderlucci
(2020) <arXiv:1902.06615v2>). There are also functions for graphical
representation of clusters obtained.

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
