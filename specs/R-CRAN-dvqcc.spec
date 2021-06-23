%global __brp_check_rpaths %{nil}
%global packname  dvqcc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Dynamic VAR - Based Control Charts for Batch Process Monitoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tsDyn 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tsDyn 

%description
A set of control charts for batch processes based on the VAR model. The
package contains the implementation of T2.var and W.var control charts
based on VAR model coefficients using the couple vectors theory. In each
time-instant the VAR coefficients are estimated from a historical
in-control dataset and a decision rule is made for online classifying of a
new batch data. Those charts allow efficient online monitoring since the
very first time-instant. The offline version is available too. In order to
evaluate the chart's performance, this package contains functions to
generate batch data for offline and online monitoring.See in Danilo
Marcondes Filho and Marcio Valk (2020) <doi:10.1016/j.ejor.2019.12.038>.

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
