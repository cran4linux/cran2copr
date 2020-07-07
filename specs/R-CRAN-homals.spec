%global packname  homals
%global packver   1.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}
Summary:          Gifi Methods for Optimal Scaling

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-grDevices 

%description
Performs a homogeneity analysis (multiple correspondence analysis) and
various extensions. Rank restrictions on the category quantifications can
be imposed (nonlinear PCA). The categories are transformed by means of
optimal scaling with options for nominal, ordinal, and numerical scale
levels (for rank-1 restrictions). Variables can be grouped into sets, in
order to emulate regression analysis and canonical correlation analysis.

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
%{rlibdir}/%{packname}/INDEX
