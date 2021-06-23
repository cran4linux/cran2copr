%global __brp_check_rpaths %{nil}
%global packname  sgee
%global packver   0.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          3%{?dist}%{?buildtag}
Summary:          Stagewise Generalized Estimating Equations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-copula 
Requires:         R-stats 
Requires:         R-utils 

%description
Stagewise techniques implemented with Generalized Estimating Equations to
handle individual, group, bi-level, and interaction selection. Stagewise
approaches start with an empty model and slowly build the model over
several iterations, which yields a 'path' of candidate models from which
model selection can be performed. This 'slow brewing' approach gives
stagewise techniques a unique flexibility that allows simple incorporation
of Generalized Estimating Equations; see Vaughan, G., Aseltine, R., Chen,
K., Yan, J., (2017) <doi:10.1111/biom.12669> for details.

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
%doc %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/INDEX
