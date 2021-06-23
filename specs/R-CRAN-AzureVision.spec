%global __brp_check_rpaths %{nil}
%global packname  AzureVision
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to Azure Computer Vision Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-AzureRMR 
BuildRequires:    R-CRAN-AzureCognitive 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
Requires:         R-CRAN-AzureRMR 
Requires:         R-CRAN-AzureCognitive 
Requires:         R-CRAN-httr 
Requires:         R-utils 

%description
An interface to 'Azure Computer Vision'
<https://docs.microsoft.com/azure/cognitive-services/Computer-vision/Home>
and 'Azure Custom Vision'
<https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/home>,
building on the low-level functionality provided by the 'AzureCognitive'
package. These services allow users to leverage the cloud to carry out
visual recognition tasks using advanced image processing models, without
needing powerful hardware of their own. Part of the 'AzureR' family of
packages.

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
