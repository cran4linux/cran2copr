%global packname  causalweight
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Estimation Methods for Causal Inference Based on InverseProbability Weighting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-np 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-np 

%description
Various estimation methods for causal inference based on inverse
probability weighting. Specifically, the package includes methods for
estimating average treatment effects as well as direct and indirect
effects in causal mediation analysis. The models refer to the studies of
Froelich (2007) <doi:10.1016/j.jeconom.2006.06.004>, Huber (2012)
<doi:10.3102/1076998611411917>, Huber (2014)
<doi:10.1080/07474938.2013.806197>, Huber (2014) <doi:10.1002/jae.2341>,
and Froelich and Huber (2017) <doi:10.1111/rssb.12232>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
