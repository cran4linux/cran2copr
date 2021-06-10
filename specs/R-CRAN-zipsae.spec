%global packname  zipsae
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Estimation with Zero-Inflated Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
This function produces empirical best linier unbiased predictions (EBLUPs)
for Zero-Inflated data and its Relative Standard Error. Small Area
Estimation with Zero-Inflated Model (SAE-ZIP) is a model developed for
Zero-Inflated data that can lead us to overdispersion situation. To handle
this kind of situation, this model is created. The model in this package
is based on Small Area Estimation with Zero-Inflated Poisson model
proposed by Dian Christien Arisona
(2018)<https://repository.ipb.ac.id/handle/123456789/92308>. For the data
sample itself, we use combination method between Roberto Benavent and
Domingo Morales (2015)<doi:10.1016/j.csda.2015.07.013> and Sabine Krieg,
Harm Jan Boonstra and Marc Smeets (2016)<doi:10.1515/jos-2016-0051>.

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
