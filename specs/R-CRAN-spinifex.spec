%global packname  spinifex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Manual Tours, Manual Control of Dynamic Projections of NumericMultivariate Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tourr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-tourr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-webshot 

%description
Generates the path for manual tours ['Cook' & 'Buja' (1997)
<doi:10.2307/1390747>]. Tours are generally available in the 'tourr'
package ['Wickham' 'et' 'al.' (2011) <doi:10.18637/jss.v040.i02>]. The
grand tour is an algorithm that shows all possible projections given
sufficient time. Guided uses projection pursuit to steer the tour towards
interesting projections. The 'spinifex' package implements manual control,
where the contribution of a selected variable can be adjusted between -1
to 1, to examine the sensitivity of structure in the data to that
variable. The result is an animation where the variable is toured into and
out of the projection completely, which can be rendered using the
'gganimate' and 'plotly' packages.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
