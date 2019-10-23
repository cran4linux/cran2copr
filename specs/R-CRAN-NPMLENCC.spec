%global packname  NPMLENCC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Non-Parametric Maximum Likelihood Estimate for Cohort Samplings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.3
Requires:         R-core >= 3.4.3
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-survival 
BuildRequires:    R-splines 
Requires:         R-MASS 
Requires:         R-survival 
Requires:         R-splines 

%description
To compute the non-parametric maximum likelihood estimates (NPMLEs) and
penalized NPMLEs with SCAD, HARD and LASSO penalties for nested
case-control or case-cohort sampling design with time matching under Cox's
regression model. It also proposes the standard error formula for
estimator using observed profile likelihood. For details about (penalized)
NPNLEs see the original paper "Penalized Full Likelihood Approach to
Variable Selection for Cox's Regression Model under Nested Case-Control
Sampling" by Wang et al. (2019) <doi:10.1007/s10985-019-09475-z>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
