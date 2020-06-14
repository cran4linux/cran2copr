%global packname  rLDCP
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Text Generation from Data

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.4
BuildRequires:    R-methods 
Requires:         R-CRAN-XML >= 3.98.1.4
Requires:         R-methods 

%description
Linguistic Descriptions of Complex Phenomena (LDCP) is an architecture and
methodology that allows us to model complex phenomena, interpreting input
data, and generating automatic text reports customized to the user needs
(see <doi:10.1016/j.ins.2016.11.002> and <doi:10.1007/s00500-016-2430-5>).
The proposed package contains a set of methods that facilitates the
development of LDCP systems. It main goal is increasing the visibility and
practical use of this research line.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/ldcpSchema.xsd
%{rlibdir}/%{packname}/INDEX
