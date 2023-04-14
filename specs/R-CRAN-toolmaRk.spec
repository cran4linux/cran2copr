%global __brp_check_rpaths %{nil}
%global packname  toolmaRk
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tests for Same-Source of Toolmarks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-dplyr >= 0.7.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-dplyr >= 0.7.2

%description
Implements two tests for same-source of toolmarks. The
chumbley_non_random() test follows the paper "An Improved Version of a
Tool Mark Comparison Algorithm" by Hadler and Morris (2017)
<doi:10.1111/1556-4029.13640>. This is an extension of the Chumbley score
as previously described in "Validation of Tool Mark Comparisons Obtained
Using a Quantitative, Comparative, Statistical Algorithm" by Chumbley et
al (2010) <doi:10.1111/j.1556-4029.2010.01424.x>.
fixed_width_no_modeling() is based on correlation measures in a diamond
shaped area of the toolmark as described in Hadler (2017).

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
