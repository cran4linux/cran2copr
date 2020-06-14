%global packname  flowr
%global packver   0.9.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.10
Release:          2%{?dist}
Summary:          Streamlining Design and Deployment of Complex Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-params >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-tools 
Requires:         R-CRAN-params >= 0.3
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-whisker 
Requires:         R-tools 

%description
This framework allows you to design and implement complex pipelines, and
deploy them on your institution's computing cluster. This has been built
keeping in mind the needs of bioinformatics workflows. However, it is
easily extendable to any field where a series of steps (shell commands)
are to be executed in a (work)flow.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/conf
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/pipelines
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
