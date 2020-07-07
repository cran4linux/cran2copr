%global packname  fmri
%global packver   1.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.3
Release:          3%{?dist}
Summary:          Analysis of fMRI Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-aws >= 2.4
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-methods 
Requires:         R-CRAN-aws >= 2.4
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-metafor 
Requires:         R-methods 

%description
Contains R-functions to perform an fMRI analysis as described in Polzehl
and Tabelow (2019) <DOI:10.1007/978-3-030-29184-6>, Tabelow et al. (2006)
<DOI:10.1016/j.neuroimage.2006.06.029>, Polzehl et al. (2010)
<DOI:10.1016/j.neuroimage.2010.04.241>, Tabelow and Polzehl (2011)
<DOI:10.18637/jss.v044.i11>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
