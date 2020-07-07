%global packname  thectar
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Hermeneutic Content Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-smacof 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-proxy 

%description
A collection of tools for performing the second step of Hermeneutic
Content Analysis (HCA; see Bergman, 2010, <doi:10.4135/9781506335193>).
The current version provides tools for implementing multidimensional
scaling (MDS) within an HCA framework. The tools offer assistance in data
preparation, modeling, and interpretation of MDS maps. The data
preparation tools help users to create similarity matrices based on
co-occurrence or sorting data. The modelling tools allow users to optimize
the modelling process by systematically calculating Stress values for a
set of p points out of n points. The tools assisting interpretation allow
users to highlight the highest similarities either per point or overall in
an MDS representation.

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
