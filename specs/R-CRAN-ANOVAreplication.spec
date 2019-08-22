%global packname  ANOVAreplication
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Test ANOVA Replications by Means of the Prior Predictive p-Value

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-quadprog 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 

%description
Allows for the computation of a prior predictive p-value to test
replication of relevant features of original ANOVA studies. Relevant
features are captured in informative hypotheses. The package also allows
for the computation of sample sizes for new studies, post-hoc power
calculations, and comes with a Shiny application in which all calculations
can be conducted as well. The statistical underpinnings are described in
Zondervan-Zwijnenburg (2019) <doi:10.31234/osf.io/6myqh>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
