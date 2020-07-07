%global packname  emma
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Evolutionary model-based multiresponse approach

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.2
Requires:         R-core >= 2.9.2
BuildArch:        noarch
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-methods 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-clusterSim 
Requires:         R-methods 

%description
The evolutionary model-based multiresponse approach (EMMA) is a novel
methodology to process optimisation and product improvement. The approach
is suitable to contexts in which the experimental cost and/or time limit
the number of implementable trials.

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
