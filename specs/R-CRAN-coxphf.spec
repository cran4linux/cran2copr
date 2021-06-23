%global __brp_check_rpaths %{nil}
%global packname  coxphf
%global packver   1.13.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cox Regression with Firth's Penalized Likelihood

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-survival 
Requires:         R-survival 

%description
Implements Firth's penalized maximum likelihood bias reduction method for
Cox regression which has been shown to provide a solution in case of
monotone likelihood (nonconvergence of likelihood function), see Heinze
and Schemper (2001) and Heinze and Dunkler (2008). The program fits
profile penalized likelihood confidence intervals which were proved to
outperform Wald confidence intervals.

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
