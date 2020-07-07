%global packname  StatRank
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}
Summary:          Statistical Rank Aggregation: Inference, Evaluation, andVisualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 

%description
A set of methods to implement Generalized Method of Moments and Maximal
Likelihood methods for Random Utility Models. These methods are meant to
provide inference on rank comparison data. These methods accept full,
partial, and pairwise rankings, and provides methods to break down full or
partial rankings into their pairwise components. Please see Generalized
Method-of-Moments for Rank Aggregation from NIPS 2013 for a description of
some of our methods.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
