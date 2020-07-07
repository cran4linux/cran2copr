%global packname  MDSPCAShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Interactive Document for Working with Multidimensional Scalingand Principal Component Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-MASS 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-dplyr 
Requires:         R-datasets 
Requires:         R-CRAN-psych 
Requires:         R-MASS 

%description
An interactive document on the topic of multidimensional scaling and
principal component analysis using 'rmarkdown' and 'shiny' packages.
Runtime examples are provided in the package function as well as at
<https://kartikeyabolar.shinyapps.io/MDS_PCAShiny/>.

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

%files
%{rlibdir}/%{packname}
