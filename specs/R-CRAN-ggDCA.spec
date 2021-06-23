%global __brp_check_rpaths %{nil}
%global packname  ggDCA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate and Plot Decision Curve

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 6.0.1
BuildRequires:    R-survival >= 3.1.12
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-CRAN-set 
BuildRequires:    R-CRAN-base.rms 
Requires:         R-CRAN-rms >= 6.0.1
Requires:         R-survival >= 3.1.12
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-do 
Requires:         R-CRAN-set 
Requires:         R-CRAN-base.rms 

%description
Diagnostic and prognostic models are typically evaluated with measures of
accuracy that do not address clinical consequences. Decision-analytic
techniques allow assessment of clinical outcomes but often require
collection of additional information and may be cumbersome to apply to
models that yield a continuous result. Decision curve analysis is a
suitable method for evaluating alternative diagnostic and prognostic
strategies that has advantages over other commonly used measures and
techniques. This method was described by Andrew J. Vickers (2006)
<doi:10.1177/0272989X06295361>.

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
