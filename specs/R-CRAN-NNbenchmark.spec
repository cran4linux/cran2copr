%global packname  NNbenchmark
%global packver   3.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Datasets and Functions to Benchmark Neural Network Packages

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-pkgload 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-pkgload 

%description
Datasets and functions to benchmark (convergence, speed, ease of use) R
packages dedicated to regression with neural networks (no classification
in this version). The templates for the tested packages are available in
the format of R, R Markdown and HTML files at
<https://github.com/pkR-pkR/NNbenchmarkTemplates> and
<https://akshajverma.com/NNbenchmarkWeb/index.html>.

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
