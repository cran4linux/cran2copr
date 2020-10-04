%global packname  metaplot
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          3%{?dist}%{?buildtag}
Summary:          Data-Driven Plot Design

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-encode >= 0.3.6
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-encode >= 0.3.6
Requires:         R-lattice 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Designs plots in terms of core structure.  See 'example(metaplot)'.
Primary arguments are (unquoted) column names; order and type (numeric or
not) dictate the resulting plot.  Specify any y variables, x variable, any
groups variable, and any conditioning variables to metaplot() to generate
density plots, boxplots, mosaic plots, scatterplots, scatterplot matrices,
or conditioned plots. Use multiplot() to arrange plots in grids. Wherever
present, scalar column attributes 'label' and 'guide' are honored,
producing fully annotated plots with minimal effort. Attribute 'guide' is
typically units, but may be encoded() to provide interpretations of
categorical values (see '?encode').  Utility unpack() transforms scalar
column attributes to row values and pack() does the reverse, supporting
tool-neutral storage of metadata along with primary data. The package
supports customizable aesthetics such as such as reference lines, unity
lines, smooths, log transformation, and linear fits. The user may choose
between trellis and ggplot output. Compact syntax and integrated metadata
promote workflow scalability.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
