%global __brp_check_rpaths %{nil}
%global packname  plantecowrap
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Enhancing Capabilities of 'plantecophys'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-plantecophys >= 1.4.4
BuildRequires:    R-CRAN-minpack.lm >= 1.2.1
BuildRequires:    R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-plantecophys >= 1.4.4
Requires:         R-CRAN-minpack.lm >= 1.2.1
Requires:         R-CRAN-tidyr >= 1.0.0

%description
Provides wrapping functions to add to capabilities to 'plantecophys'
(Duursma, 2015, <doi:10.1371/journal.pone.0143346>). Key added
capabilities include temperature responses of mesophyll conductance (gm,
gmeso), apparent Michaelis-Menten constant for rubisco carboxylation in
air (Km, Kcair),and photorespiratory CO2 compensation point (GammaStar)
for fitting A-Ci or A-Cc curves for C3 plants (for temperature responses
of gm, Km, & GammaStar, see Bernacchi et al., 2002,
<doi:10.1104/pp.008250>; for theory on fitting A-Ci or A-Cc curves, see
Farquhar et al., 1980; <doi:10.1007/BF00386231>, von Caemmerer, 2000,
ISBN:064306379X; Ethier & Livingston, 2004
<doi:10.1111/j.1365-3040.2004.01140.x>; and Gu et al., 2010,
<doi:10.1111/j.1365-3040.2010.02192.x>). Includes the ability to fit the
Arrhenius and modified Arrhenius temperature response functions (see
Medlyn et al., 2002, <doi:10.1046/j.1365-3040.2002.00891.x>) for maximum
rubisco carboxylation rates (Vcmax) and maximum electron transport rates
(Jmax) (see Farquhar et al., 1980; <doi:10.1007/BF00386231>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
