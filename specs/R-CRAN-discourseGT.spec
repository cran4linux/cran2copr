%global packname  discourseGT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Analyze Group Patterns using Graph Theory in EducationalSettings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ggplot2 

%description
Analyzes group patterns using discourse analysis data with graph theory
mathematics. Takes the order of which individuals talk and converts it to
a network edge and weight list. Returns the density, centrality,
centralization, and subgroup information for each group. Based on the
analytical framework laid out in Chai et al. (2019)
<doi:10.1187/cbe.18-11-0222>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
