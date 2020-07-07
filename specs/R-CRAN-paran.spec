%global packname  paran
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          3%{?dist}
Summary:          Horn's Test of Principal Components/Factors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
An implementation of Horn's technique for numerically and graphically
evaluating the components or factors retained in a principle components
analysis (PCA) or common factor analysis (FA). Horn's method contrasts
eigenvalues produced through a PCA or FA on a number of random data sets
of uncorrelated variables with the same number of variables and
observations as the experimental or observational data set to produce
eigenvalues for components or factors that are adjusted for the sample
error-induced inflation. Components with adjusted eigenvalues greater than
one are retained. paran may also be used to conduct parallel analysis
following Glorfeld's (1995) suggestions to reduce the likelihood of
over-retention.

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
