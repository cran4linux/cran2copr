%global packname  GVARX
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}%{?buildtag}
Summary:          Perform Global Vector Autoregression Estimation and Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-tsDyn 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-tsDyn 

%description
Perform the estimation and inference of Global Vector Autoregression model
(GVAR) of Pesaran, Schuermann and Weiner (2004)
<DOI:10.1198/073500104000000019> and Dees, di Mauro, Pesaran and Smith
(2007) <DOI:10.1002/jae.932>.

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
