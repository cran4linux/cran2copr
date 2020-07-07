%global packname  crs
%global packver   0.15-31.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15.31.1
Release:          3%{?dist}
Summary:          Categorical Regression Splines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-rgl 
Requires:         R-boot 
Requires:         R-stats 
Requires:         R-CRAN-np 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-rgl 

%description
Regression splines that handle a mix of continuous and categorical
(discrete) data often encountered in applied settings. I would like to
gratefully acknowledge support from the Natural Sciences and Engineering
Research Council of Canada (NSERC, <http://www.nserc-crsng.gc.ca>), the
Social Sciences and Humanities Research Council of Canada (SSHRC,
<http://www.sshrc-crsh.gc.ca>), and the Shared Hierarchical Academic
Research Computing Network (SHARCNET, <https://www.sharcnet.ca>).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
