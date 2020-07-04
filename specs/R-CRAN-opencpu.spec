%global packname  opencpu
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Producing and Reproducing Results

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.0
BuildRequires:    R-CRAN-sys >= 2.1
BuildRequires:    R-CRAN-remotes >= 2.0.2
BuildRequires:    R-CRAN-knitr >= 1.6
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-httpuv >= 1.3
BuildRequires:    R-CRAN-webutils >= 0.6
BuildRequires:    R-CRAN-evaluate >= 0.12
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-protolite 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-curl >= 4.0
Requires:         R-CRAN-sys >= 2.1
Requires:         R-CRAN-remotes >= 2.0.2
Requires:         R-CRAN-knitr >= 1.6
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-httpuv >= 1.3
Requires:         R-CRAN-webutils >= 0.6
Requires:         R-CRAN-evaluate >= 0.12
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-protolite 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-openssl 

%description
A system for embedded scientific computing and reproducible research with
R. The OpenCPU server exposes a simple but powerful HTTP api for RPC and
data interchange with R. This provides a reliable and scalable foundation
for statistical services or building R web applications. The OpenCPU
server runs either as a single-user development server within the
interactive R session, or as a multi-user Linux stack based on Apache2.
The entire system is fully open source and permissively licensed. The
OpenCPU website has detailed documentation and example apps.

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
