%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3fairness
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fairness Auditing and Debiasing for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-data.table >= 1.13.6
BuildRequires:    R-CRAN-mlr3 >= 0.13.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-mlr3measures 
BuildRequires:    R-CRAN-mlr3misc 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-data.table >= 1.13.6
Requires:         R-CRAN-mlr3 >= 0.13.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-mlr3measures 
Requires:         R-CRAN-mlr3misc 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-ggplot2 

%description
Integrates fairness auditing and bias mitigation methods for the 'mlr3'
ecosystem. This includes fairness metrics, reporting tools, visualizations
and bias mitigation techniques such as "Reweighing" described in 'Kamiran,
Calders' (2012) <doi:10.1007/s10115-011-0463-8> and "Equalized Odds"
described in 'Hardt et al.' (2016)
<https://papers.nips.cc/paper/2016/file/9d2682367c3935defcb1f9e247a97c0d-Paper.pdf>.
Integration with 'mlr3' allows for auditing of ML models as well as
convenient joint tuning of machine learning algorithms and debiasing
methods.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
