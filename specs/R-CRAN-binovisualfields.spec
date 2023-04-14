%global __brp_check_rpaths %{nil}
%global packname  binovisualfields
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Depth-Dependent Binocular Visual Fields Simulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-shiny 

%description
Simulation and visualization depth-dependent integrated visual fields.
Visual fields are measured monocularly at a single depth, yet real-life
activities involve predominantly binocular vision at multiple depths. The
package provides functions to simulate and visualize binocular visual
field impairment in a depth-dependent fashion from monocular visual field
results based on Ping Liu, Allison McKendrick, Anna Ma-Wyatt, Andrew
Turpin (2019) <doi:10.1167/tvst.9.3.8>. At each location and depth plane,
sensitivities are linearly interpolated from corresponding locations in
monocular visual field and returned as the higher value of the two. Its
utility is demonstrated by evaluating DD-IVF defects associated with 12
glaucomatous archetypes of 24-2 visual field pattern in the included
'shiny' apps.

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
%{rlibdir}/%{packname}
