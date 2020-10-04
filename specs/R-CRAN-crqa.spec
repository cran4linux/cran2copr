%global packname  crqa
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Recurrence Quantification Analysis for Categorical andContinuous Time-Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tseriesChaos 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rdist 
Requires:         R-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tseriesChaos 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rdist 

%description
Auto, Cross and Multi-dimensional recurrence quantification analysis.
Different methods for computing recurrence, cross vs. multidimensional or
profile iti.e., only looking at the diagonal recurrent points, as well as
functions for optimization and plotting are proposed. in-depth measures of
the whole cross-recurrence plot, Please refer to by Coco and Dale (2014)
<doi:10.3389/fpsyg.2014.00510> and Wallot (2018)
<doi:10.1080/00273171.2018.1512846> for further details about the method.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
