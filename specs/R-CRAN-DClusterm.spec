%global packname  DClusterm
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Model-Based Detection of Disease Clusters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-DCluster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-parallel 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-DCluster 
Requires:         R-methods 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-latticeExtra 

%description
Model-based methods for the detection of disease clusters using GLMs,
GLMMs and zero-inflated models. These methods are described in 'V.
Gómez-Rubio et al.' (2019) <doi:10.18637/jss.v090.i14> and 'V. Gómez-Rubio
et al.' (2018) <doi:10.1007/978-3-030-01584-8_1>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/samples
%{rlibdir}/%{packname}/INDEX
