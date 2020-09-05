%global packname  MFPCA
%global packver   1.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Functional Principal Component Analysis for Data Observed on Different Dimensional Domains

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.3.4
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-mgcv >= 1.8.33
BuildRequires:    R-CRAN-funData >= 1.3.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
Requires:         R-mgcv >= 1.8.33
Requires:         R-CRAN-funData >= 1.3.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-irlba 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
Calculate a multivariate functional principal component analysis for data
observed on different dimensional domains. The estimation algorithm relies
on univariate basis expansions for each element of the multivariate
functional data (Happ & Greven, 2018) <doi:10.1080/01621459.2016.1273115>.
Multivariate and univariate functional data objects are represented by S4
classes for this type of data implemented in the package 'funData'. For
more details on the general concepts of both packages and a case study,
see Happ-Kurz (2020) <doi:10.18637/jss.v093.i05>.

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
