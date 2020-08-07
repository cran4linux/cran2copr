%global packname  NTS
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Nonlinear Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-CRAN-dlm 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MSwM 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-parallel 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tensor 
Requires:         R-base 
Requires:         R-CRAN-dlm 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-MSwM 
Requires:         R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-tensor 

%description
Simulation, estimation, prediction procedure, and model identification
methods for nonlinear time series analysis, including threshold
autoregressive models, Markov-switching models, convolutional functional
autoregressive models, nonlinearity tests, Kalman filters and various
sequential Monte Carlo methods. More examples and details about this
package can be found in the book "Nonlinear Time Series Analysis" by Ruey
S. Tsay and Rong Chen, John Wiley & Sons, 2018 (ISBN: 978-1-119-26407-1).

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
