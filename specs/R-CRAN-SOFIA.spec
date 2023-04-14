%global __brp_check_rpaths %{nil}
%global packname  SOFIA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Making Sophisticated and Aesthetical Figures in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-png 
BuildRequires:    R-grid 
Requires:         R-CRAN-png 
Requires:         R-grid 

%description
Software that leverages the capabilities of Circos by manipulating data,
preparing configuration files, and running the Perl-native Circos directly
from the R environment with minimal user intervention. Circos is a novel
software that addresses the challenges in visualizing genetic data by
creating circular ideograms composed of tracks of heatmaps, scatter plots,
line plots, histograms, links between common markers, glyphs, text, and
etc. Please see <http://www.circos.ca>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
